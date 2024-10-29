import { useEffect, useState } from 'react'
import { setUser } from '../utils/auth'

const MainWrapper = ({ children }) => {
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const handler = async () => {
      setLoading(true)
      setUser()
      setLoading(false)
    }
    handler()
  }, [])
  return <>{loading ? null : children}</>
}

export default MainWrapper
