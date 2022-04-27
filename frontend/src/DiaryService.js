import axios from 'axios';
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

    createPost(post) {
        const url = `${API_URL}/posts/create`;
		return axios.post(url, post);
    }
    
}