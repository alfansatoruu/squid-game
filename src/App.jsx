import { useState } from 'react'
import axios from 'axios'

function App() {
  const [count, setCount] = useState(0)
  const [output, setOutput] = useState('')
  const [loading, setLoading] = useState(false)

  const runPythonScript = async () => {
    setLoading(true)
    try {
      const response = await axios.post('http://localhost:5000/run-python')
      const data = response.data
      
      if (data.success) {
        setOutput(data.output)
      } else {
        setOutput(`Error: ${data.error}`)
      }
    } catch (error) {
      setOutput(`Request failed: ${error.message}`)
    }
    setLoading(false)
  }
}

export default App