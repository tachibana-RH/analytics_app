import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';

import SignIn from '../views/SignIn.vue';
import SignUp from '../views/SignUp.vue'
import Menu from '../views/Menu.vue'

Vue.use(VueRouter);

const routes: RouteConfig[] = [
  {
    path: '/',
    name: 'SignIn',
    component: SignIn,
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
    // // route level code-splitting
    // // this generates a separate chunk (about.[hash].js) for this route
    // // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/menu',
    name: 'Menu',
    component: Menu,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
