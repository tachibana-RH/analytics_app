import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';

import SignIn from '../views/SignIn.vue';
import SignUp from '../views/SignUp.vue';
import Menu from '../views/menu/Top.vue';
import CreateNewClient from '../views/menu/CreateNewClient.vue';

import { ApiRqsV1 } from '../methods/ApiRequestV1'

Vue.use(VueRouter);

const routes: RouteConfig[] = [
  {
    path: '/',
    name: 'signin',
    component: SignIn,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp,
    // // route level code-splitting
    // // this generates a separate chunk (about.[hash].js) for this route
    // // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/menu',
    name: 'menu',
    component: Menu,
    // children: [
    //   {
    //     name: 'menu.create',
    //     path: '/create',
    //     component: CreateNewClient,
    //     meta: { requiresAuth: true }
    //   }
    // ],
    meta: { requiresAuth: true }
  },
  {
    name: 'menu.create',
    path: '/create',
    component: CreateNewClient,
    meta: { requiresAuth: true }
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    ApiRqsV1('POST', '/auth/refresh', {}, true)
    .then(res => {
      next();
    })
    .catch(err => {
      next({ path: '/', query: { redirect: to.fullPath }});
    });
  } else {
    next();
  }
});

export default router;
