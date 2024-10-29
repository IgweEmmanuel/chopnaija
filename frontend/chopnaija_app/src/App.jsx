// import Navbar from './components/ui/NavBar'
// import ProductPage from './pages/Product'
// const App = () => {
//   return (
//     <div>
//       <Navbar />
//       <ProductPage />
//     </div>
//   )
// }

// export default App

import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ProductPage from './pages/Product'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/product/:slug" element={<ProductPage />} />
        {/* other routes */}
      </Routes>
    </BrowserRouter>
  )
}

export default App
