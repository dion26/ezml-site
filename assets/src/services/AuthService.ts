import axios from "axios";

const API_URL = "/api/dj-rest-auth/";

class AuthService {
  login(email: string, password: string) {
    return axios
      .post(API_URL + "signin", { email, password })
      .then((response) => {
        if (response.data.accessToken) {
          localStorage.setItem("user", JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  logout() {
    localStorage.removeItem("user");
  }

  register(firstname: string, lastname:string, email: string, password1: string, password2: string) {
    return axios.post(API_URL + "signup", {
      firstname,
      lastname,
      email,
      password1,
      password2,
    });
  }
}

export default new AuthService();