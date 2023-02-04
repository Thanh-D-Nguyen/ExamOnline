<template>
	<div id="login">
		<el-container>
			<el-header>
				<h1 style="color: #FFFFFF;margin-top: 50px;">Python online test system</h1>
			</el-header>
			<el-main>
				<div id="login-from">
					<el-form ref="loginForm" status-icon :model="loginForm" :rules="rules">
						<el-form-item label="student ID" prop="username">
							<el-input v-model="loginForm.username" autocomplete="off"></el-input>
							</el-input>
						</el-form-item>
						<el-form-item label="password" prop="password">
							<el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
							</el-input>
						</el-form-item>
						<slide-verification @check-result="checkResult"></slide-verification>
						<br />
						<el-button type="primary" @click.native.prevent="handLogin('loginForm')">Log in</el-button>
						<div class="text-foot">
							No account yet?
							<router-link to="/register" class="register-link">
								register
							</router-link>
						</div>
					</el-form>
				</div>
			</el-main>
		</el-container>
	</div>
</template>

<script>
	import SlideVerification from '@/components/SlideVerification.vue'
	export default {
		data() {
			return {
				confirmSuccess: false,
				loginForm: {
					username: null,
					password: null,
				},
				rules: {
					username: [{
						required: true,
						message: 'Please enter the school number',
						trigger: 'blur'
					}],
					password: [{
						required: true,
						message: 'Please enter the password',
						trigger: 'blur'
					}]
				}
			}
		},
		components:{
			SlideVerification
		},
		methods: {
			//Get slider verification results
			checkResult(message) {
				this.confirmSuccess = message
			},
			//Process login
			handLogin(formName) {
				//Clean up cache information
				localStorage.clear()
				sessionStorage.clear()
				if (this.confirmSuccess) {
					const msg = this
					this.$refs[formName].validate((valide) => {
						if (valide) {
							axios.post(`api/jwt-auth/`, this.loginForm).then(res => {
								console.log(res); //处理成功的函数 相当于success
								if (res.status == 200) {
									this.$message({
										message: 'login successful',
										type: 'success'
									});
									this.$store.commit("setUser", res.data.user)
									this.$store.commit("setStudent", res.data.student)
									this.$store.commit("setAuthorization", res.data.token)
									this.$router.push('/exam')
								}
							}).catch(function(error) {
								//Error treatment is equivalent to ERROR
								msg.$message('Login failure, account number or password error');
								console.log(error) 
							});
						} else {
							//Form verification failed
						}
					});
				} else {
					//Failure to verify
					this.$message('Please drag the slider for verification!');
				}
			}
		}
	}
</script>

<style lang="scss" scoped>
	#login {
		height: 700px;
		// background-color: #244d6f;
		background-image: url(../assets/bg.jpg);
		background-repeat: no-repeat;
		background-size: cover; 
	}

	#login-from {
		margin: 50px 540px;
		width: 400px;
		height: 400px;
		border-radius: 10px;
		background-color: #FFFFFF;
	}

	.el-form {
		padding-top: 50px;
		margin: 50px 50px;
		width: 300px;
	}

	.el-input {

	}

	.el-button {
		width: 100%;
	}
	
	.text-foot {
		// text-align: center;
		// padding: 10px;
		font-weight: 700;
		margin-top: 20px;
		// color: var(--color-semidark);
	}
</style>
