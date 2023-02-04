import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '@/layout/index.vue'

Vue.use(VueRouter)

const routes = [{
		path: '/',
		component: Layout,
		redirect: '/exam',
		children: [{
				path: 'exam',
				component: () => import('../views/Exam.vue'),
				name: 'exam',
				meta: {
					title: 'examination centre'
				}
			},
			{
				path: 'practice',
				name: 'Practice',
				component: () => import('../views/Practice.vue'),
				meta: {
					title: 'Simulation exercise'
				}
			},
			{
				path: 'grade',
				name: 'Grade',
				component: () => import('../views/Grade.vue'),
				meta: {
					title: 'Query score'
				}
			},
			{
				path: 'center',
				name: 'Center',
				component: () => import('../views/Center.vue'),
				meta: {
					title: 'Personal center'
				}
			},
			{
				path: 'password',
				name: 'Password',
				component: () => import('../views/Password.vue'),
				meta: {
					title: 'change Password'
				}
			},
			{
				path: 'paper',
				name: 'Paper',
				component: () => import('../views/Paper.vue'),
				meta: {
					title: 'Test papers details'
				}
			},
			{
				path: 'score',
				name: 'Score',
				component: () => import('../views/Score.vue'),
				meta: {
					title: 'Test score'
				}
			}
		]
	},
	{
		path: '/answer',
		name: 'Answer',
		component: () => import('../views/Answer.vue'),
		meta: {
			title: 'Answer interface '
		}
	},
	{
		path: '/record',
		name: 'Record',
		component: () => import('../views/Record.vue'),
		meta: {
			title: 'Practice record'
		}
	},
	{
		path: '/login',
		name: 'Login',
		component: () => import('../views/Login.vue'),
		meta: {
			title: 'login interface'
		}
	},
	{
		path: '/register',
		name: 'Register',
		component: () => import('../views/Register.vue'),
		meta: {
			title: 'Registration interface'
		}
	},
	{
		path: '*',
		name: 'Error',
		component: () => import('../views/Error.vue'),
		meta: {
			title: '404 error interface'
		}
	}
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

// 导航守卫
// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
router.beforeEach((to, from, next) => {
	// 设置标题
	if (to.meta.title) {
		document.title = to.meta.title
	}

	if (to.path === '/login' || to.path === '/register') {
		next();
	} else {
		let token = sessionStorage.getItem('Authorization');
		if (token === null || token === '') {
			next('/login');
		} else {
			next();
		}
	}
});
export default router
