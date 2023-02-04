<template>
	<div id="register">
		<el-container>
			<el-header>
				<h1 style="color: #FFFFFF;margin-top: 50px;">Python online test system</h1>
			</el-header>
			<el-main>
				<div id="register-from">
					<el-form ref="registerForm" status-icon :model="registerForm" :rules="rules">
						<el-form-item label="Student ID" prop="username">
							<el-input v-model="registerForm.username" autocomplete="off"></el-input>
							</el-input>
						</el-form-item>
						<el-form-item label="Name" prop="name">
							<el-input v-model="registerForm.name" autocomplete="off"></el-input>
							</el-input>
						</el-form-item>
						<el-form-item label="Password" prop="password">
							<el-input type="password" v-model="registerForm.password" autocomplete="off"></el-input>
							</el-input>
						</el-form-item>
						<el-form-item label="Confirm Password" prop="checkpwd">
							<el-input type="password" v-model="registerForm.checkpwd" autocomplete="off"></el-input>
							</el-input>
						</el-form-item>
						<slide-verification @check-result="checkResult"></slide-verification>
						<br />
						<el-button type="primary" @click.native.prevent="handRegister('registerForm')">register</el-button>
						<div class="text-foot">
							Existing account?
							<router-link to="/login" class="login-link">
								Log in
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
			var validatePass = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('Please enter the password'));
				} else {
					if (this.registerForm.checkpwd !== '') {
						this.$refs.registerForm.validateField('checkpwd');
					}
					callback();
				}
			};
			var validatePass2 = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('Please enter the password again'));
				} else if (value !== this.registerForm.password) {
					callback(new Error('Two input passwords are inconsistent!'));
				} else {
					callback();
				}
			};
			return {
				confirmSuccess: false,
				registerForm: {
					username: null,
					password: null,
					checkpwd: null,
					name: null,
				},
				rules: {
					username: [{
							required: true,
							message: 'Please enter the school number',
							trigger: 'blur'
						},
						{
							min: 6,
							max: 15,
							message: 'The length is 6 to 15 characters',
							trigger: 'blur'
						}
					],
					password: [{
							required: true,
							message: 'Please enter the password',
							trigger: 'blur'
						},
						{
							min: 6,
							max: 10,
							message: 'The length is 6 to 15 characters',
							trigger: 'blur'
						},
						{
							validator: validatePass,
							trigger: 'blur'
						}
					],
					checkpwd: [{
							required: true,
							message: 'Please enter the password again',
							trigger: 'blur'
						},
						{
							min: 6,
							max: 15,
							message: 'The length is 6 to 10 characters',
							trigger: 'blur'
						},
						{
							validator: validatePass2,
							trigger: 'blur'
						}
					],
					name: [{
							required: true,
							message: 'Please type in your name',
							trigger: 'blur'
						},
						{
							min: 2,
							max: 10,
							message: 'The length is from 2 to 8 characters',
							trigger: 'blur'
						}
					]
				}
			}
		},
		components: {
			SlideVerification
		},
		methods: {
			//Get slider verification results
			checkResult(message) {
				this.confirmSuccess = message
			},
			//Processing
			handRegister(formName) {
				if (this.confirmSuccess) {
					const msg = this
					this.$refs[formName].validate((valide) => {
						if (valide) {
							axios.post(`api/register/`, this.registerForm).then(res => {
								console.log(res); //The function of successful processing is equivalent tosuccess
								if (res.status == 200) {
									this.$message({
										message: 'registration success',
										type: 'success'
									});
									this.$router.push('/login')
								} else {
									this.$message({
										message: res.data.msg,
										type: 'error'
									});
								}
							}).catch(function(error) {
								msg.$message('registration failed');
								console.log(error) //Error treatment is equivalent toerror
							});
						} else {
							//Form verification failed
						}
					});
				} else {
					//Failure to verify
					this.$message('Please drag the slider for verification！');
				}
			}
		}
	}
</script>

<style lang="scss" scoped>
	#register {
		// height: 700px;
		/* background-color: #244d6f; */
		background-image: url(../assets/bg.jpg);
		background-repeat: no-repeat;
		background-size: cover;
	}

	#register-from {
		margin: 0px 540px;
		width: 400px;
		height: 600px;
		border-radius: 10px;
		background-color: #FFFFFF;
	}

	.el-form {
		padding-top: 20px;
		margin: 50px 50px;
		width: 300px;
	}

	.el-input {}

	.el-button {
		width: 100%;
	}

	.text-foot {
		font-weight: 700;
		margin-top: 20px;
	}
</style>
