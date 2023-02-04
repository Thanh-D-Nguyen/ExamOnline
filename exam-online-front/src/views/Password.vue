<template>
	<div id="password">
		<el-form ref="pwdForm" status-icon :model="pwdForm" :rules="rules">
			<h1>change Password</h1>
			<el-form-item label="Old password" prop="oldpwd">
				<el-input v-model="pwdForm.oldpwd" autocomplete="off"></el-input>
				</el-input>
			</el-form-item>
			<el-form-item label="New Password" prop="newpwd">
				<el-input type="password" v-model="pwdForm.newpwd" autocomplete="off"></el-input>
				</el-input>
			</el-form-item>
			<el-form-item label="Confirm new Password" prop="checkpwd">
				<el-input type="password" v-model="pwdForm.checkpwd" autocomplete="off"></el-input>
				</el-input>
			</el-form-item>
			<el-button type="primary" @click.native.prevent="updatePwd('pwdForm')">Confirm the change</el-button>
			<el-button @click="cancel">Cancel</el-button>
		</el-form>
	</div>
</template>

<script>
	export default {
		data() {
			var validatePass = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('Please enter the password'));
				} else {
					if (this.pwdForm.checkpwd !== '') {
						this.$refs.pwdForm.validateField('checkpwd');
					}
					callback();
				}
			};
			var validatePass2 = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('Please enter the password again'));
				} else if (value !== this.pwdForm.newpwd) {
					callback(new Error('Two input passwords are inconsistent!'));
				} else {
					callback();
				}
			};
			return {
				pwdForm: {
					oldpwd: null,
					newpwd: null,
					checkpwd: null,
					userid: null
				},
				rules: {
					oldpwd: [{
						required: true,
						message: 'Please enter the original password',
						trigger: 'blur'
					}],
					newpwd: [{
							required: true,
							message: 'Please enter the password',
							trigger: 'blur'
						},
						{
							min: 6,
							max: 10,
							message: 'The length is 6 to 15 characters ',
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
					]
				}
			}
		},
		computed: {
			getType() {
				return this.$route.params.type;
			}
		},
		methods: {
			updatePwd(formName) {
				this.$refs[formName].validate((valide) => {
					if (valide) {
						this.$axios.patch(
							`/api/update-pwd/?format=json`,
							this.pwdForm
						).then(res => {
							console.log(res)
							if (res.status == 200 && res.data.msg == 'success') {
								this.$message({
									message: 'Update password success',
									type: 'success'
								});
							} else {
								this.$message({
									message: 'The original password is incorrect, and the update failed',
									type: 'error'
								});
							}
						}).catch(error => {
							console.log(error)
						})
					} else {
						//Form verification failed
					}
				});
			},
			cancel() {
				this.$router.push('/')
			}
		},
		created() {
			this.pwdForm.userid = this.$route.params.student.user
		}
	}
</script>

<style lang="scss" scoped>
	#password {}

	.el-form {
		margin-left: 350px;
		width: 400px;
	}

	.el-select {
		width: 320px;
	}

	.el-input {}
</style>
