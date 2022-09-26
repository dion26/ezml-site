
interface UserAuth {
    accessToken: string,
}

export default function authHeader() {
    
    var userJson = localStorage.getItem('user');
    const user = JSON.parse(userJson || "{}");
  
    if (user && user.accessToken) {
      return { Authorization: 'Bearer ' + user.accessToken };
    } else {
      return undefined;
    }
  }