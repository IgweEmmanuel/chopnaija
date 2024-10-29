import { Navigate, Outlet } from 'react-router-dom'
// import { userAuthStore } from '../store/auth';
import Cookie from 'js-cookie'
import jwt_decode from 'jwt-decode'

const isAccessTokenExpired = (access_token) => {
  try {
    const decodedToken = jwt_decode(access_token)
    return decodedToken.exp < Date.now() / 1000
  } catch (error) {
    console.log(error)
    return true
  }
}

const ProtectedRoute = () => {
  const access_token = Cookie.get('access_token')
  const refresh_token = Cookie.get('refresh_token')

  const isAuthenticated = () => {
    if (!access_token || !refresh_token) {
      return false
    }
    return !isAccessTokenExpired(access_token)
  }

  return isAuthenticated() ? <Outlet /> : <Navigate to="/login" />
}

export default ProtectedRoute
