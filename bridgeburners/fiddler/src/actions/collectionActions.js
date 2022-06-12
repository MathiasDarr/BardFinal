import { endpoint } from 'app/api';
import asyncActionCreator from './asyncActionCreator';
import { queryEndpoint } from './util';

export const queryCollections = asyncActionCreator(query => async () => queryEndpoint(query), { name: 'QUERY_COLLECTIONS'} );
export const getCollecti


export const fetchCollections = asyncActionCreator(({ id, refresh }) => async () => {
    const config = { params: { refresh } };
    const response = await endpoint.get('bard', config);
    return { id, data: response.data };
  }, { name: 'GET_COLLECTIONS'});
  