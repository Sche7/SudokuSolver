import Vue from "vue";
import VueRouter from "vue-router";
import SolveBoard from '../components/SolveBoard.vue';

Vue.useAttrs(VueRouter)

const routes = [
    {
        path: '/solve/:board_id',
        name: 'SolveBoard',
        component: SolveBoard,
    }
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router