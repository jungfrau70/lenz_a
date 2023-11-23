<template>
  <div>
    <h2>Download File in Vue JS using Axios</h2>
    <template v-for="(filesrc, index) in filesrcs" :key="index">
      <button  @click="downloadWithAxios(filesrc.src, filesrc.title)" target>Download</button>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      filesrcs: [
        { title: 'c.docx', src: 'http://127.0.0.1:5000/static/documents/c.docx' },
      ],
    }
  },
  methods: {
    forceFileDownload(response, title) {
      console.log(title)
      const url = window.URL.createObjectURL(new Blob([response.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', title)
      document.body.appendChild(link)
      link.click()
    },
    downloadWithAxios(url, title) {
      axios({
        method: 'GET',
        url,
        responseType: 'blob',
        // responseType: 'arraybuffer',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, PUT, POST, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token',
          'Access-Control-Allow-Credentials': 'false',
        }
      })
        .then((response) => {
          this.forceFileDownload(response, title)
        })
        .catch(() => console.log('error occured'))
    },
  }
}
</script>