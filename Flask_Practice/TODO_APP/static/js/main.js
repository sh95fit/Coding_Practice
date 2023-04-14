// console.log('javascript link test')

const { createApp } = Vue

const TaskApp = {
  data() {
    return {
      message : "Flask Vue test",
      task : "",
      tasks : [
        {title: 'One'},
        {title: 'Two'}
      ]
    }
  },
  delimiters : ['[[', ']]']
}

createApp(TaskApp).mount('#app')