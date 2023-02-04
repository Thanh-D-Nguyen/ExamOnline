<template>
	<div id="exam">
		<el-row type="flex" justify="center">
			<el-col :span="4">
				<el-input v-model="key" placeholder="Please enter the test name" prefix-icon="el-icon-search" clearable></el-input>
			</el-col>
			<el-col :span="4">
				<el-button type="primary" @click="searchExam()">Search test paper</el-button>
			</el-col>
		</el-row>
		</el-row>
		<el-row>
			<h3 style="border-left: solid 10px rgb(220, 208, 65);">Test list</h3>
			<div style="padding-left: 15px">
				<el-col :span="4" v-for="(item, index) in pagination.results" :key="index" :offset="index > 0 ? 1 : 0">
					<el-card :body-style="{ padding: '0px' }" v-loading="loading">
						<img src="@/assets/exam.png" class="image">
						<div style="padding: 14px;">
							<span>{{item.name}}</span>
							<p>
								<span>examination time：{{item.exam_date}}</span>
								<br />
								<span>Exam duration:{{item.total_time}}minute</span>
							</p>
							<div class="bottom clearfix">
								<!-- <router-link target="_blank" :to="{path:'/answer',query:{exam: pagination.results[index],paper:item.paper}}">
									<el-button type="text" class="button">Start doing the question </el-button>
								</router-link> -->
								<el-button type="text" class="button" @click="toAnswer(index)">Start doing questions</el-button>
							</div>
						</div>
					</el-card>
				</el-col>
			</div>
		</el-row>
		<Pagination :count="pagination.count" @size-change="handleSizeChange" @current-change="handleCurrentChange"></Pagination>
	</div>
</template>

<script>
	import Pagination from '@/components/Pagination.vue'
	export default {
		data() {
			return {
				loading: false,
				key: null,
				page: 1,
				page_size: 5,
				pagination: {
					count: null,
					next: null,
					previous: null,
					results: []
				}
			}
		},
		components: {
			Pagination
		},
		methods: {
			//Get test information
			getExamInfo() {
				this.$axios(`/api/exams/?format=json`, {
					params: {
						page: this.page,
						page_size: this.page_size,
						student_id: this.$store.state.student.id,
					}
				}).then(res => {
					this.pagination = res.data
					this.loading = false
					// console.log(this.pagination)
				}).catch(error => {
					console.log(error)
				})
			},
			//Change the number per page
			handleSizeChange(val) {
				// console.log(`Each page $ {val}`);
				this.page_size = val
				this.searchExam()
			},
			//How many pages jump to
			handleCurrentChange(val) {
				// console.log(`current page: ${val}`);
				this.page = val
				this.searchExam()
			},
			//Search exam
			searchExam() {
				if (this.key) {
					this.$axios(`/api/exams/?format=json`, {
						params: {
							page: this.page,
							page_size: this.page_size,
							search: this.key,
							student_id: this.$store.state.student.id,
						}
					}).then(res => {
						if (res.status == 200) {
							this.pagination = res.data
						}
					})
				} else {
					this.getExamInfo()
				}
			},
			//Jump to the answer page
			toAnswer(index) {
				//Use LocalStorage to store test information and test paper information
				localStorage.removeItem('exam');
				localStorage.removeItem('paper');
				sessionStorage.removeItem('isPractice')
				localStorage.setItem("exam", JSON.stringify(this.pagination.results[index]));
				localStorage.setItem("paper", JSON.stringify(this.pagination.results[index].paper));
				this.$store.commit("setIsPractice", false)
				this.$router.push({
					path: '/answer',
					query: {}
				})
			}
		},
		created() {
			this.getExamInfo()
			this.loading = true
		}
	}
</script>
<style lang="scss" scoped>
	.bottom {
		margin-top: 13px;
		line-height: 12px;
	}

	.button {
		padding: 0;
		// float: right;
	}

	.image {
		width: 50%;
		height: 80%;
		display: block;
		margin: 20px auto 10px auto;
	}

	.clearfix:before,
	.clearfix:after {
		display: table;
		content: "";
	}

	.clearfix:after {
		clear: both
	}
</style>
