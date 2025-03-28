import axios from 'axios';
import {returnErrors} from './messages';
import {
    CATEGORIES_LOADED,
    EVENTS_ERROR,
    EVENTS_LOADED,
    EVENTS_LOADING,
    SET_CATEGORY
} from "./types";

export const loadEvents = (categoryId) => (dispatch) => {
    dispatch({type: EVENTS_LOADING});
    axios.get(`api/events/categoryEvents/${categoryId}`)
        .then(res => {
            dispatch({
                type: EVENTS_LOADED,
                payload: res.data.events
            })
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
            dispatch({
                type: EVENTS_ERROR
            });
        })
};

export const loadCategories = (categoryId) => (dispatch) => {
    dispatch({type: EVENTS_LOADING});
    axios.get(`api/events/categories/${categoryId}`)
        .then(res => {
            dispatch({
                type: CATEGORIES_LOADED,
                payload: res.data.subcategories
            })
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
            dispatch({
                type: EVENTS_ERROR
            });
        })
};

export const setCategory = (category) => (dispatch) => {
    dispatch({
        type: SET_CATEGORY,
        payload: {
            category: category
        }
    });
};