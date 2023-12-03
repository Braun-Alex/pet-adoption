import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

const initialState = {
    isAuthenticated: false,
    user: null,
    shelter: null,
    entityType: '',
    entityName: '',
    setAuthHeader: () => {},
    saveTokens: () => {},
    getData: () => {},
    tryRefreshAccessToken: () => {},
    getUserData: () => {},
    getShelterData: () => {},
    tryLoginUser: () => {},
    tryLoginShelter: () => {},
    logout: () => {}
};

export const AuthContext = createContext(initialState);

export const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(true);
    const [user, setUser] = useState(null);
    const [shelter, setShelter] = useState(null);
    const [entityType, setEntityType] = useState('');
    const [entityName, setEntityName] = useState('');

    const setAuthHeader = (accessToken) => {
        axios.defaults.headers.common['Authorization'] = accessToken ? `Bearer ${accessToken}` : '';
    };

    const saveTokens = (data) => {
        const accessToken = data.access_token;
        localStorage.setItem('access_token', accessToken);
        localStorage.setItem('refresh_token', data.refresh_token);
        setAuthHeader(accessToken);
    }

    const getData = async (apiUrl) => {
        try {
            const response = await axios.get(apiUrl);
            return response.data;
        } catch (error) {
            const accessToken = localStorage.getItem('access_token');
            if (accessToken) {
                const success = await tryRefreshAccessToken();
                if (success) {
                    try {
                        const response = await axios.get(apiUrl);
                        return response.data;
                    } catch(error) {
                        return null;
                    }
                }
            }
        }
    }

    const tryRefreshAccessToken = async () => {
        const refreshToken = localStorage.getItem('refresh_token');
        try {
            setAuthHeader(refreshToken);
            const response = await axios.get('http://127.0.0.1:8000/api/v1/token/refresh');
            const accessToken = response.data.access_token;
            localStorage.setItem('access_token', accessToken);
            setAuthHeader(accessToken);
            return true;
        } catch (error) {
            logout();
            return false;
        }
    }

    const getUserData = async () => {
        const user = await getData('http://127.0.0.1:8080/api/v1/users/profile');
        if (user) {
            return {
                userID: user.id,
                userFullName: user.full_name,
                userEmail: user.email
            };
        }
        return null;
    }

    const getShelterData = async () => {
        const shelter = await getData('http://127.0.0.1:8080/api/v1/shelter/profile');
        if (shelter) {
            return {
                shelterID: shelter.id,
                shelterName: shelter.full_name,
                shelterEmail: shelter.email
            };
        }
        return null;
    }

    const tryLoginUser = async () => {
        const userData = await getUserData();
        if (userData) {
            setUser(userData);
            setEntityType('user');
            setEntityName(userData.userFullName);
            setIsAuthenticated(true);
            return true;
        }
        return false;
    }

    const tryLoginShelter = async () => {
        const shelterData = await getShelterData();
        if (shelterData) {
            setShelter(shelterData);
            setEntityType('shelter');
            setEntityName(shelterData.shelterName);
            setIsAuthenticated(true);
            return true;
        }
        return false;
    }

    const logout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        setAuthHeader(null);
        setUser(null);
        setShelter(null);
        setEntityType('');
        setEntityName('');
        setIsAuthenticated(false);
    }

    useEffect(() => {
        const getAuthState = async () => {
            const access_token = localStorage.getItem('access_token');
            setAuthHeader(access_token);
            let success = false;
            if (access_token) {
                success = await tryLoginUser();
                if (!success) {
                    success = await tryLoginShelter();
                }
            }
            setIsAuthenticated(success);
        };

        getAuthState();
    }, []);

    return (
        <AuthContext.Provider value={{ isAuthenticated, user, shelter, entityType, entityName, saveTokens, tryLoginUser, tryLoginShelter, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
