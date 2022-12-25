import Vue from "vue";
import VueRouter from "vue-router";
import SolveBoard from '../components/SudokuBoard.vue';

Vue.useAttrs(VueRouter)

const routes = [
    {
        path: '/solve',
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
