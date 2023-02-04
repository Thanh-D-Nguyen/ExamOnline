<template>
	<div class="center">
		<el-form ref="centerForm" status-icon :model="centerForm" :rules="rules" label-width="80px">
			<h1>个人中心</h1>
			<el-form-item label="Name" prop="name">
				<el-input v-model="centerForm.name"></el-input>
			</el-form-item>
			<el-form-item label="gender" prop="gender">
				<el-select v-model="centerForm.gender" placeholder="Please choose gender ">
					<el-option label="Male" value="m"></el-option>
					<el-option label="Female" value="f"></el-option>
				</el-select>
			</el-form-item>
			<!-- <el-form-item label="年级" prop="year">
				<el-select v-model="centerForm.year" placeholder="请选择年级">
					<el-option label="2016级" value="2016"></el-option>
					<el-option label="2017级" value="2017"></el-option>
					<el-option label="2018级" value="2018"></el-option>
					<el-option label="2019级" value="2019"></el-option>
				</el-select>
			</el-form-item>
			<el-form-item label="专业" prop="major">
				<el-input v-model="centerForm.major"></el-input>
			</el-form-item> -->
			<el-form-item label="Class" prop="clazz">
				<el-select v-model="centerForm.clazz" placeholder="Please select grade ">
					<el-option v-for="item in clazzOptions" :key="item.id" :label="item.year + item.major + item.clazz" :value="item.id">
					</el-option>
				</el-select>
			</el-form-item>
			<el-form-item>
				<el-button type="primary" @click="updateInfo('centerForm')">Confirm the changes</el-button>
				<el-button @click="cancel">Cancel</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				centerForm: {
					name: null,
					gender: null,
					year: null,
					major: null,
					clazz: null,
					clazz_id: null,
					user: null
				},
				clazzOptions: [], //Class drop -down data
				rules: {
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
					],
					gender: [{
						required: true,
						message: 'Please select gender',
						trigger: 'change'
					}],
					// year: [{
					// 	required: true,
					// 	message: 'Please select grade',
					// 	trigger: 'change'
					// }],
					// major: [{
					// 		required: true,
					// 		message: 'Please enter the professional',
					// 		trigger: 'blur'
					// 	},
					// 	{
					// 		min: 8,
					// 		max: 30,
					// 		message: 'Length from 8 to 30 characters',
					// 		trigger: 'blur'
					// 	}
					// ],
					clazz: [{
							required: true,
							message: 'Please select the class',
							trigger: 'change'
						},
					]
				}
			}
		},
		methods: {
			updateInfo(formName) {
				this.$refs[formName].validate((valide) => {
					if (valide) {
						this.centerForm.clazz_id = this.centerForm.clazz;
						this.$axios.patch(
							`/api/students/${this.centerForm.id}/?format=json`,
							this.centerForm
						).then(res => {
							console.log(res)
							if (res.status == 200) {
								this.$message({
									message: 'Update personal information success',
									type: 'success'
								});
								//更新缓存
								this.$store.commit("sestStudent", this.centerForm)
							} else {
								this.$message({
									type: 'Update personal information failure',
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
			// Get class information
			getClazzInfo() {
				this.$axios(`/api/clazzs/?format=json`, {
					// params: {
					// }
				}).then(res => {
					console.log(res.data)
					this.clazzOptions = res.data
				}).catch(error => {
					console.log(error)
				})
			},
			cancel() {
				this.$router.push('/')
			}
		},
		created() {
			this.centerForm = this.$store.state.student;
			this.getClazzInfo()
		}
	}
</script>

<style lang="scss" scoped>
	#center {}

	.el-form {
		margin-left: 350px;
		width: 400px;
	}

	.el-select {
		width: 320px;
	}

	.el-input {}
</style>
