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
    loginUser: () => {},
    loginShelter: () => {},
    logout: () => {}
};

export const AuthContext = createContext(initialState);

export const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [user, setUser] = useState(null);
    const [shelter, setShelter] = useState(null);
    const [entityType, setEntityType] = useState('');
    const [entityName, setEntityName] = useState('')

    const setAuthHeader = (accessToken) => {
        axios.defaults.headers.common['Authorization'] = accessToken ? `Bearer ${accessToken}` : '';
    };

    const saveTokens = (serverResponse) => {
        localStorage.setItem('access_token', serverResponse.data.access_token);
        localStorage.setItem('refresh_token', serverResponse.data.refresh_token);
        setAuthHeader(serverResponse.data.access_token);
    }

    const getData = (apiUrl) => {
        axios.get(apiUrl).then(response => {
            return response.data;
        }).catch(() => {
            const accessToken = localStorage.getItem('access_token');
            if (accessToken) {
                const success = tryRefreshAccessToken();
                if (success) {
                    this.getData();
                }
            }
        });
        return null;
    }

    const tryRefreshAccessToken = () => {
        const refreshToken = localStorage.getItem('refresh_token');
        axios.post('http://127.0.0.1:8000/token/refresh',
            { refresh_token: refreshToken }).then(response => {
            localStorage.setItem('access_token', response.data.access_token);
            this.setAuthHeader(response.data.access_token);
            return true;
        });
        return false;
    }

    const getUserData = () => {
        const user = getData('http://127.0.0.1:8080/api/v1/user/profile');
        if (user) {
            return {
                userID: user.id,
                userFullName: user.full_name,
                userEmail: user.email
            }
        }
        return null
    }

    const getShelterData = () => {
        const shelter = getData('http://127.0.0.1:8080/api/v1/shelter/profile');
        if (shelter) {
            return {
                shelterID: shelter.id,
                shelterName: shelter.name,
                shelterEmail: shelter.email,
                shelterNumber: shelter.number
            }
        }
        return null
    }

    const loginUser = () => {
        setIsAuthenticated(true);
        setUser(getUserData());
        setEntityType('user');
        setEntityName(user.fullName);
    };

    const loginShelter = () => {
        setIsAuthenticated(true);
        setShelter(getShelterData());
        setEntityType('shelter');
        setEntityName(shelter.name);
    };

    const tryLoginUser = () => {
        const user = getUserData();
        if (user) {
            loginUser();
            return true;
        }
        return false;
    }

    const tryLoginShelter = () => {
        const shelter = getShelterData();
        if (shelter) {
            loginShelter();
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
    }

    useEffect(() => {
        const access_token = localStorage.getItem('access_token');
        if (access_token) {
            let success = tryLoginUser();
            if (!success) {
                success = tryLoginShelter();
            }
            if (success) {
                setIsAuthenticated(true);
            }
        }
    }, []);

    return (
        <AuthContext.Provider value={{ isAuthenticated, user, shelter, entityType, entityName, loginUser, loginShelter, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
