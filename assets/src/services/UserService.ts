import axios from 'axios';
import authHeader from './authHeader';

const API_URL = '/api/';

type User = {
    pk: number;
    username: string;
    email: string;
    firstname: string;
    lastname: string;
  };

type GetUsersResponse = {
    data: User[];
  };

class UserService {
  getPublicContent() {
    return axios.get(API_URL);
  }

  getUserBoard() {
    return axios.get<GetUsersResponse>(API_URL + 'user', { headers: authHeader() });
  }
}

export default new UserService();