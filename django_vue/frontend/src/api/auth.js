import client from './client'

export default {
  login: authInfo => {
    return new Promise((resolve, reject) => {
      client.post('/blog-auth/', authInfo)
        .then(res => resolve({ token: res.data.token }))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message))
        })
    })
  }
}
