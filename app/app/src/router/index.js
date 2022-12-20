import Vue from "vue";
import VueRouter from "vue-router";
import Solve from '../components/Solve.vue';

Vue.useAttrs(VueRouter)

const routes = [
    {
        path: '/solve/:board_id',
        name: 'Solve',
        component: Solve,
    }
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router
