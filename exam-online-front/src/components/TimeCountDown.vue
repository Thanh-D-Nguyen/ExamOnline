<template>
	<div>
		<div style="text-align:center;color:red;">
			<h2>{{showTimeLeft}}</h2>
		</div>
	</div>
</template>
<script>
	export default {
		name: "timeCountDown",
		props: {
			totalTime: Number,
		},
		data() {
			return {
				timeLeft: 0,
				bundleIntervalEvent: ""
			};
		},
		computed: {
			//Use the calculation attribute to display the result
			showTimeLeft() {
				//The remaining seconds <= 0
				if (this.timeLeft <= 0) {
					// End Event
					this.$emit('hand-in', true)
					return "Exam time has arrived";
				}
				// The remaining seconds> 0
				else {
					let day = Math.floor(this.timeLeft / 86400);
					let hour = Math.floor((this.timeLeft % 86400) / 3600);
					let min = Math.floor(((this.timeLeft % 86400) % 3600) / 60);
					let sec = Math.floor(((this.timeLeft % 86400) % 3600) % 60);
					// return (day + "天  " + (hour < 10 ? "0" : "") + hour + ": " + (min < 10 ? "0" : "") + min + ": " + (sec < 10 ? "0" :
					// 	"") + sec);
					return ("Countdown " + (hour < 10 ? "0" : "") + hour + ": " + (min < 10 ? "0" : "") + min + ": " + (sec < 10 ? "0" :
						"") + sec);
				}
			}
		},
		methods: {
			//Initize the minute into seconds
			initSecondsLeft() {
				// let currentDate = new Date();
				// let tmp = this.endDate.split(/[- : /]/);
				// let toEndDate = new Date(tmp[0], tmp[1] - 1, tmp[2], tmp[3], tmp[4], tmp[5]);
				//参数日期 > 当前日期 => 获取剩余秒数
				// if (toEndDate > currentDate) {
				// 	// this.timeLeft = Math.floor((toEndDate.getTime() - currentDate.getTime()) / 1000);
				// 	this.timeLeft = Math.floor((toEndDate.getTime() - currentDate.getTime()) / 1000);
				// } else {
				// 	this.timeLeft = 0;
				// }
				this.timeLeft = this.totalTime * 60;
			},
			//Division event: The remaining seconds-, when the remaining seconds are 0, the interval incident is cleared.
			intervalEvent() {
				if (this.timeLeft > 0) {
					this.timeLeft--;
				} else {
					clearInterval(this.bundleIntervalEvent);
				}
			},
		},
		mounted() {},
		created() {
			//Initialize the remaining seconds
			this.initSecondsLeft();
			//Executive intervals.
			this.bundleIntervalEvent = setInterval(this.intervalEvent, 1000);
		},
		beforeDestroy() {
			clearInterval(this.bundleIntervalEvent);
		}
	};
</script>
