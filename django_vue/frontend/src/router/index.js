import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

function loadView (view) {
  return () => import(`@/views/${view}.vue`)
}

const routes = [
  {
    path: '/',
    name: 'main',
    component: loadView('Main')
  },
  {
    path: '/posts/',
    redirect: '/'
  },
  {
    path: '/posts/:postId/',
    name: 'postDetail',
    component: loadView('MainDetail')
  },
  {
    path: '/posts/tags/',
    redirect: '/'
  },
  {
    path: '/posts/tags/:tagId/',
    name: 'tagFilter',
    component: loadView('Main')
  },
  {
    path: '/auth',
    name: 'Auth',
    component: loadView('MainAuth')
  }

]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
