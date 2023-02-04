<template>
	<div id="grade">
		<el-table :data="pagination.results" style="width: 100%" v-loading="loading" border>
			<el-table-column type="index" width="50">
			</el-table-column>
			<el-table-column prop="creat_time" label="Papers" sortable>
				<template slot-scope="scope">
					<i class="el-icon-time"></i>
					<span style="margin-left: 10px">{{ scope.row.create_time.replace('T', ' ').substring(0, 19) }}</span>
				</template>
			</el-table-column>
			<el-table-column prop="exam.name" label="Test name" width="300">
				<template slot-scope="scope">
					<el-popover trigger="hover" placement="top">
						<p>Test name: {{ scope.row.exam.name }}</p>
						<p>Exam date: {{ scope.row.exam.exam_date }}</p>
						<p>Exam duration: {{ scope.row.exam.total_time }}</p>
						<p>Their profession: {{ scope.row.exam.major }}</p>
						<p>Exam Instructions: {{ scope.row.exam.tips }}</p>
						<div slot="reference" class="name-wrapper">
							<el-tag size="medium">{{ scope.row.exam.name }}</el-tag>
						</div>
					</el-popover>
				</template>
			</el-table-column>
			<el-table-column prop="score" label="Score" width="150" sortable>
				<template slot-scope="scope">
					<i class="el-icon-trophy"></i>
					<span style="margin-left: 10px">{{ scope.row.score }}</span>
				</template>
			</el-table-column>
			<el-table-column prop="exam.exam_date" label="Examination time" width="180" sortable>
				<template slot-scope="scope">
					<i class="el-icon-time"></i>
					<span style="margin-left: 10px">{{ scope.row.exam.exam_date }}</span>
				</template>
			</el-table-column>
			<el-table-column prop="score" label="Filter" width="200" :filters="[{ text: 'Pass', value: 'pass' }, { text: 'Failed', value: 'fail' }]"
			 :filter-method="filterScore" filter-placement="bottom-end">
				<template slot-scope="scope">
					<el-tag v-if="scope.row.score >= 60" type="success" disable-transitions>Pass</el-tag>
					<el-tag v-if="scope.row.score < 60" type="warning" disable-transitions>Failed</el-tag>
				</template>
			</el-table-column>
		</el-table>
		<Pagination :count="pagination.count" @size-change="handleSizeChange" @current-change="handleCurrentChange"></Pagination>
	</div>
</template>

<script>
	import Pagination from '@/components/Pagination.vue'
	export default {
		data() {
			return {
				loading: false,
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
		created() {
			this.getGradeInfo()
			this.loading = true
		},
		methods: {
			//Get results information
			getGradeInfo() {
				this.$axios(`api/grades/?format=json`, {
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
			//Filtering and failure
			filterScore(value, row) {
				if (value === 'pass') {
					return row.score >= 60;
				} else if (value === 'fail') {
					return row.score < 60
				} else {
					return row.score > 0
				}
			},
			//Change the number per page
			handleSizeChange(val) {
				// console.log(`Each page $ {val}`);
				this.page_size = val
				this.getGradeInfo()
			},
			//How many pages jump to
			handleCurrentChange(val) {
				// console.log(`current page: ${val}`);
				this.page = val
				this.getGradeInfo()
			}
		}
	}
</script>

<style>

</style>
