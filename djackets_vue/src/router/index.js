import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

import store from '../store'


import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from "@/views/Search";
import Cart from "@/views/Cart";
import SingUp from "@/views/SingUp";
import LogIn from "@/views/LogIn";
import MyAccount from "@/views/MyAccount";
import Checkout from "@/views/Checkout";
import Success from "@/views/Success";


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
    {
    path: '/sing-up',
    name: 'SingUp',
    component: SingUp
  },
    {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
    {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta:{
       requireLogin : true
    }
  },

    {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
    {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
    {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta:{
       requireLogin : true
    }
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
    {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: {to: to.path}})
  } else{
    next()
  }
})

export default router
