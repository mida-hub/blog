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
    path: '/category',
    name: 'category',
    component: loadView('PostDetail')
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
