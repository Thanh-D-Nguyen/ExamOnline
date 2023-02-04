<template>
	<div id="record">
		<div id="choice-record" class="type">
			<h2>Choice</h2>
			<div class="question" v-for="(item,index) in choiceRecord">
				<h4>{{index + 1}}. {{item.choice.question}}</h4>
				<el-radio-group v-model="item.your_answer" disabled>
					<el-radio label="A">A. {{item.choice.answer_A}}</el-radio><br />
					<el-radio label="B">B. {{item.choice.answer_B}}</el-radio><br />
					<el-radio label="C">C. {{item.choice.answer_C}}</el-radio><br />
					<el-radio label="D">D. {{item.choice.answer_D}}</el-radio><br />
				</el-radio-group>
				<h4>Result:
					<el-tag :type="item.choice.right_answer === item.your_answer ? 'success' : 'danger'">
						{{item.choice.right_answer === item.your_answer ? "Correct" : "Mistake"}}
					</el-tag>
				</h4>
				<h4>Correct answer:{{item.choice.right_answer}}</h4>
				<h4>Fraction:{{item.choice.score}}</h4>
				<h4>Difficulty:<el-rate v-model="item.choice.level" disabled="" style="float: right;margin-right: 1140px;"></el-rate>
				</h4>
				<h4>Analyze:{{item.choice.analysis}}</h4>
			</div>
		</div>
		<div id="fill-record" class="type">
			<h2>Blank</h2>
			<div class="question" v-for="(item,index) in fillRecord">
				<h4>{{index + 1}}. {{item.fill.question}}</h4>
				<el-input v-model="item.your_answer" disabled></el-input>
				<h4>Result:
					<el-tag :type="item.fill.right_answer === item.your_answer ? 'success' : 'danger'">
						{{item.fill.right_answer === item.your_answer ? "Correct" : "Mistake"}}
					</el-tag>
				</h4>
				<h4>Correct answer:{{item.fill.right_answer}}</h4>
				<h4>Fraction:{{item.fill.score}}</h4>
				<h4>Difficulty:<el-rate v-model="item.fill.level" disabled="" style="float: right;margin-right: 1140px;"></el-rate>
				</h4>
				<h4>Analyze:{{item.fill.analysis}}</h4>
			</div>
		</div>
		<div id="judge-record" class="type">
			<h2>True or False</h2>
			<div class="question" v-for="(item,index) in judgeRecord">
				<h4>{{index + 1}}. {{item.judge.question}}</h4>
				<el-radio-group v-model="item.your_answer" disabled>
					<el-radio label="T" border>Correct</el-radio><br />
					<el-radio label="F" border>False</el-radio><br />
				</el-radio-group>
				<h4>Result:
					<el-tag :type="item.judge.right_answer === item.your_answer ? 'success' : 'danger'">
						{{item.judge.right_answer === item.your_answer ? "Correct" : "Mistake"}}
					</el-tag>
				</h4>
				<h4>Correct answer:{{item.judge.right_answer}}</h4>
				<h4>Fraction:{{item.judge.score}}</h4>
				<h4>Difficulty:<el-rate v-model="item.judge.level" disabled="" style="float: right;margin-right: 1140px;"></el-rate>
				</h4>
				<h4>Analyze:{{item.judge.analysis}}</h4>
			</div>
		</div>
		<div id="program-record" class="type">
			<h2>Programming</h2>
			<div class="question" v-for="(item,index) in programRecord">
				<h4>{{index + 1}}. {{item.program.question}}</h4>
				<el-row type="flex" justify="space-around">
					<el-col :span="10">
						Programming area
						<el-input type="textarea" :autosize="{ minRows: 18, maxRows: 18}" v-model="item.your_answer" disabled>
						</el-input>
					</el-col>
					<el-col :span="10">
						Output information
						<el-input type="textarea" :autosize="{ minRows: 18, maxRows: 18}" v-model="item.cmd_msg" disabled>
						</el-input>
					</el-col>
				</el-row>
				<h4>Result:
					<el-tag :type="item.cmd_msg === 'pass' ? 'success' : 'danger'">
						{{item.cmd_msg === 'pass' ? "正确" : "错误"}}
					</el-tag>
				</h4>
				<!-- <h4>正确答案:{{item.program.right_answer}}</h4> -->
				<h4>Fraction:{{item.program.score}}</h4>
				<h4>Difficulty:<el-rate v-model="item.program.level" disabled="" style="float: right;margin-right: 1140px;"></el-rate>
				</h4>
				<h4>Analyze:{{item.program.analysis}}</h4>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				choiceRecord: [], //Selected questions practice record
				fillRecord: [], //Fill in the blank questions practice record
				judgeRecord: [], //Judgment questions practice record
				programRecord: [], //Programming questions practice record
			}
		},
		created() {
			this.getChoiceRecordInfo();
			this.getFillRecordInfo();
			this.getJudgeRecordInfo();
			this.getProgramRecordInfo();
		},
		methods: {
			//Get selection questions practice record
			getChoiceRecordInfo() {
				this.$axios(`api/records/choices/?format=json`, {
					params: {
						page: this.page,
						page_size: this.page_size,
						practice_id: this.$route.query.practice_id,
					}
				}).then(res => {
					this.loading = false
					this.choiceRecord = res.data
				}).catch(error => {
					console.log(error)
				})
			},
			//Get selection questions practice record
			getFillRecordInfo() {
				this.$axios(`api/records/fills/?format=json`, {
					params: {
						page: this.page,
						page_size: this.page_size,
						practice_id: this.$route.query.practice_id,
					}
				}).then(res => {
					this.loading = false
					this.fillRecord = res.data
				}).catch(error => {
					console.log(error)
				})
			},
			//Get judgment exercise practice record
			getJudgeRecordInfo() {
				this.$axios(`api/records/judges/?format=json`, {
					params: {
						page: this.page,
						page_size: this.page_size,
						practice_id: this.$route.query.practice_id,
					}
				}).then(res => {
					this.loading = false
					this.judgeRecord = res.data
				}).catch(error => {
					console.log(error)
				})
			},
			//Get programming questions
			getProgramRecordInfo() {
				this.$axios(`api/records/programs/?format=json`, {
					params: {
						page: this.page,
						page_size: this.page_size,
						practice_id: this.$route.query.practice_id,
					}
				}).then(res => {
					this.loading = false
					this.programRecord = res.data
				}).catch(error => {
					console.log(error)
				})
			},
		}
	}
</script>

<style lang="scss" scoped>
	#record {
		// background-color: #13CE66;
	}

	.type {
		text-align: center;
		// background-color: #0195FF;
	}

	.question {
		text-align: left;
		margin-left: 200px;
	}
	
	.el-input {
		max-width: 800px;
	}
</style>
