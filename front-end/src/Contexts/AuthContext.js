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
            console.log(response); // Тестові логи
            return /*JSON.parse(*/response.data;//);
        } catch (error) {
            const accessToken = localStorage.getItem('access_token');
            if (accessToken) {
                const success = await tryRefreshAccessToken();
                if (success) {
                    return getData(apiUrl);
                }
            }
        }
        return null;
    }

    const tryRefreshAccessToken = async () => {
        const refreshToken = localStorage.getItem('refresh_token');
        try {
            const response = await axios.post('http://127.0.0.1:8080/api/v1/token/refresh', { refresh_token: refreshToken });
            const accessToken = response.data.access_token;
            localStorage.setItem('access_token', accessToken);
            setAuthHeader(response.data.accessToken);
            return true;
        } catch (error) {
            return false;
        }
    }

    const getUserData = async () => {
        const user = await getData('http://127.0.0.1:8080/api/v1/users/profile');
        //console.log(user);
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
        //console.log("tryloginuser1");
        const userData = await getUserData();
       // console.log("tryloginuser2");
       // console.log(userData);
        if (userData) {
            //console.log(userData);
            setUser(userData);
           // console.log("tryloginuser3");
            setEntityType('user');
            //console.log("tryloginuser4");
            setEntityName(userData.userFullName);
           // console.log("tryloginuser5");
            setIsAuthenticated(true);
           // console.log("tryloginuser6");
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
        setIsAuthenticated(false);
    }

    useEffect(() => {
        const getAuthState = async () => {
            //console.log("test1");
            const access_token = localStorage.getItem('access_token');
           // console.log("test2");
            setAuthHeader(access_token);
           // console.log("test3");
            let success = false;
            if (access_token) {
              //  console.log("test4");
                success = await tryLoginUser();
               // console.log(success);
                if (!success) {
                   // console.log("test5");
                    success = await tryLoginShelter();
                    console.log(success);
                }
            }
           // console.log("test6");
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
