import axios from 'axios';
// const apiEndpoint = document.documentElement.getAttribute('data-api-endpoint')


export const endpoit = axios.create({
    baseURL: process.env.REACT_APP_API_ENDPOINT,
    headers: {},
    paramsSerializer: queryString.stringify
});