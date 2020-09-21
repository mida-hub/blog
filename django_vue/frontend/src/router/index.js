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
    path: '/post/:postId',
    name: 'postDetail',
    component: loadView('MainDetail')
  },
  {
    path: '*',
    component: loadView('Main')
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
