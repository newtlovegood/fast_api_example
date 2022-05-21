import axios, { AxiosRequestConfig } from 'axios';
const API_URL = 'http://localhost:8000';

export default class CustomersService{
	
	constructor(){}

    getPosts() {
        const url = `${API_URL}/posts/`;
		return axios.get(url).then(response => response.data);
    }

    getPost(post_id) {
        const url = `${API_URL}/posts/${post_id}`;
        return axios.get(url).then(response => response.data);
    }

    createPost(token, post) {
        const url = `${API_URL}/posts/create`;
        const bearer = 'Bearer ' + token;
        console.log(post);
        return axios.post(url, post, {headers: {'accept': 'application/json', 'Authorization': bearer }});
        // return fetch(`${API_URL}/posts/create`, {
        //     method: 'POST',
        //     headers: {
        //         'accept': 'application/json',
        //         'Authorization': bearer 
        //     },
            
        // }).then(response => response.json())
    }
    
}