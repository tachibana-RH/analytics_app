import axios, { AxiosResponse, Method } from 'axios';

export function ApiRqsV1(_method: Method, _url: string, _data: object | undefined, isRefresh: boolean): Promise<AxiosResponse> {
  axios.defaults.xsrfHeaderName = "X-CSRF-TOKEN"
  if (isRefresh) {
    axios.defaults.xsrfCookieName = 'csrf_refresh_token';
  } else {axios.defaults.xsrfCookieName = 'csrf_access_token';}
  
  return axios.request({
    method: _method,
    url: process.env.VUE_APP_API_ORIGIN + '/api/v1' + _url,
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
    responseType: 'json',
    withCredentials: true,
    data: _data
  });
}