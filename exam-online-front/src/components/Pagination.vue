<template>
	<div id="pagination">
		<el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="page" :page-sizes="[5, 10]"
		 :page-size="page_size" layout="total, sizes, prev, pager, next, jumper" :total="count">
		</el-pagination>
	</div>
</template>

<script>
	export default {
		name: 'pagination',
		data() {
			return {
				page: 1,
				page_size: 5
			}
		},
		props: {
			count: Number,
		},
		methods: {
			//Change the number per page
			handleSizeChange(val) {
				console.log(`Each page $ {val}`);
				this.page_size = val
				this.$emit('size-change', val)
			},
			//How many pages jump to
			handleCurrentChange(val) {
				// console.log(`$current page: ${val}`);
				this.page = val
				this.$emit('current-change', val)
			}
		}
	}
</script>

<style  lang="scss" scoped>
	#pagination {
		margin-top: 30px;
	}
</style>
