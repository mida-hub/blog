import * as types from './mutation-types'
import { Auth } from '../api'

export default {
  login: ({ commit }, authInfo) => {
    return Auth.login(authInfo)
      .then(({ token }) => {
        commit(types.AUTH_LOGIN, { token })
        localStorage.setItem('token', token)
      })
      .catch(err => { throw err })
  },
  logout: ({ commit }) => {
    commit(types.AUTH_LOGOUT, { token: null})
    localStorage.removeItem('token')
  }
}
