// // components/ProductPage.jsx
// import { useState } from 'react'
// import { Star, Minus, Plus, Heart, Share2, ShoppingCart } from 'lucide-react'
// import { Alert, AlertDescription } from '../components/ui/Alert'

// const ProductPage = () => {
//   const [quantity, setQuantity] = useState(1)
//   const [showAlert, setShowAlert] = useState(false)

//   const product = {
//     name: 'Organic Fresh Avocados',
//     price: 4.99,
//     unit: 'each',
//     rating: 4.8,
//     reviews: 128,
//     description:
//       'Farm-fresh, hand-picked avocados sourced directly from local organic farmers. Rich in healthy fats and perfect for your favorite recipes.',
//     details: ['100% Organic', 'Locally Sourced', 'Pesticide-free', 'Non-GMO'],
//     nutrition: {
//       calories: '160',
//       fat: '15g',
//       protein: '2g',
//       carbs: '9g',
//     },
//   }

//   const handleAddToCart = () => {
//     setShowAlert(true)
//     setTimeout(() => setShowAlert(false), 3000)
//   }

//   return (
//     <div className="min-h-screen bg-gray-50">
//       <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
//         <div className="bg-white rounded-2xl shadow-lg overflow-hidden">
//           <div className="md:flex">
//             {/* Product Image */}
//             <div className="md:w-1/2">
//               <div className="relative h-96 md:h-full">
//                 <img
//                   src="https://images.unsplash.com/photo-1519162808019-7de1683fa2ad?ixlib=rb-4.0.3"
//                   alt="Fresh Avocados"
//                   className="w-full h-full object-cover"
//                 />
//                 <button className="absolute top-4 right-4 p-2 rounded-full bg-white/80 hover:bg-white">
//                   <Heart className="w-6 h-6 text-teal-600" />
//                 </button>
//               </div>
//             </div>

//             {/* Product Info */}
//             <div className="md:w-1/2 p-8">
//               <div className="flex justify-between items-start">
//                 <div>
//                   <h1 className="text-3xl font-bold text-gray-900">
//                     {product.name}
//                   </h1>
//                   <div className="mt-2 flex items-center">
//                     <div className="flex items-center">
//                       {[...Array(5)].map((_, i) => (
//                         <Star
//                           key={i}
//                           className={`w-5 h-5 ${
//                             i < Math.floor(product.rating)
//                               ? 'text-yellow-400 fill-current'
//                               : 'text-gray-300'
//                           }`}
//                         />
//                       ))}
//                     </div>
//                     <span className="ml-2 text-gray-600">
//                       ({product.reviews} reviews)
//                     </span>
//                   </div>
//                 </div>
//                 <button className="p-2 rounded-full bg-gray-100 hover:bg-gray-200">
//                   <Share2 className="w-5 h-5 text-gray-600" />
//                 </button>
//               </div>

//               <div className="mt-6">
//                 <p className="text-gray-600">{product.description}</p>
//               </div>

//               <div className="mt-8">
//                 <div className="flex items-center justify-between">
//                   <span className="text-2xl font-bold text-teal-600">
//                     ${product.price}
//                     <span className="text-sm font-normal text-gray-500">
//                       /{product.unit}
//                     </span>
//                   </span>
//                   <div className="flex items-center space-x-4">
//                     <button
//                       onClick={() => setQuantity(Math.max(1, quantity - 1))}
//                       className="p-2 rounded-full bg-gray-100 hover:bg-gray-200"
//                     >
//                       <Minus className="w-4 h-4 text-gray-600" />
//                     </button>
//                     <span className="text-xl font-medium text-gray-900">
//                       {quantity}
//                     </span>
//                     <button
//                       onClick={() => setQuantity(quantity + 1)}
//                       className="p-2 rounded-full bg-gray-100 hover:bg-gray-200"
//                     >
//                       <Plus className="w-4 h-4 text-gray-600" />
//                     </button>
//                   </div>
//                 </div>
//               </div>

//               <button
//                 onClick={handleAddToCart}
//                 className="mt-8 w-full bg-teal-600 text-white py-4 px-6 rounded-lg flex items-center justify-center space-x-2 hover:bg-teal-700 transition duration-200"
//               >
//                 <ShoppingCart className="w-5 h-5" />
//                 <span>Add to Cart</span>
//               </button>

//               {/* Product Details */}
//               <div className="mt-8">
//                 <h3 className="text-lg font-semibold text-gray-900">
//                   Product Details
//                 </h3>
//                 <ul className="mt-4 space-y-2">
//                   {product.details.map((detail, index) => (
//                     <li key={index} className="flex items-center text-gray-600">
//                       <span className="w-2 h-2 bg-teal-600 rounded-full mr-2"></span>
//                       {detail}
//                     </li>
//                   ))}
//                 </ul>
//               </div>

//               {/* Nutrition Info */}
//               <div className="mt-8">
//                 <h3 className="text-lg font-semibold text-gray-900">
//                   Nutrition Information
//                 </h3>
//                 <div className="mt-4 grid grid-cols-2 gap-4">
//                   {Object.entries(product.nutrition).map(([key, value]) => (
//                     <div key={key} className="bg-gray-50 p-3 rounded-lg">
//                       <div className="text-sm text-gray-500 capitalize">
//                         {key}
//                       </div>
//                       <div className="text-lg font-semibold text-gray-900">
//                         {value}
//                       </div>
//                     </div>
//                   ))}
//                 </div>
//               </div>
//             </div>
//           </div>
//         </div>

//         {/* Alert */}
//         {showAlert && (
//           <div className="fixed bottom-4 right-4">
//             <Alert className="bg-teal-600 text-white">
//               <AlertDescription>
//                 Product added to cart successfully!
//               </AlertDescription>
//             </Alert>
//           </div>
//         )}
//       </div>
//     </div>
//   )
// }

// export default ProductPage

// components/ProductPage.jsx
import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { Star, Minus, Plus, Heart, Share2, ShoppingCart } from 'lucide-react'
import { Alert, AlertDescription } from '../components/ui/Alert'
import axios from 'axios'

const ProductPage = () => {
  const { slug } = useParams()
  const [product, setProduct] = useState(null)
  const [quantity, setQuantity] = useState(1)
  const [showAlert, setShowAlert] = useState(false)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/api/products/${slug}/`
        )
        setProduct(response.data)
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    fetchProduct()
  }, [slug])

  const handleAddToCart = () => {
    setShowAlert(true)
    setTimeout(() => setShowAlert(false), 3000)
  }

  if (loading)
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-2xl text-gray-600">Loading...</div>
      </div>
    )

  if (error)
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-xl text-red-600">Error: {error}</div>
      </div>
    )

  if (!product)
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-xl text-gray-600">Product not found</div>
      </div>
    )

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="bg-white rounded-2xl shadow-lg overflow-hidden">
          <div className="md:flex">
            {/* Product Image */}
            <div className="md:w-1/2">
              <div className="relative h-96 md:h-full">
                <img
                  src={
                    product.images.length > 0
                      ? `${product.images}`
                      : 'https://via.placeholder.com/600x600'
                  }
                  alt={product.name}
                  className="w-full h-full object-cover"
                />
                <button className="absolute top-4 right-4 p-2 rounded-full bg-white/80 hover:bg-white">
                  <Heart className="w-6 h-6 text-teal-600" />
                </button>
              </div>
            </div>

            {/* Product Info */}
            <div className="md:w-1/2 p-8">
              <div className="flex justify-between items-start">
                <div>
                  <div className="text-sm text-teal-600 mb-2">
                    {product.category.name}
                  </div>
                  <h1 className="text-3xl font-bold text-gray-900">
                    {product.name}
                  </h1>
                  <div className="mt-2 flex items-center">
                    <div className="flex items-center">
                      {[...Array(5)].map((_, i) => (
                        <Star
                          key={i}
                          className={`w-5 h-5 ${
                            i < Math.floor(product.rating)
                              ? 'text-yellow-400 fill-current'
                              : 'text-gray-300'
                          }`}
                        />
                      ))}
                    </div>
                    <span className="ml-2 text-gray-600">
                      ({product.reviews_count} reviews)
                    </span>
                  </div>
                </div>
                <button className="p-2 rounded-full bg-gray-100 hover:bg-gray-200">
                  <Share2 className="w-5 h-5 text-gray-600" />
                </button>
              </div>

              <div className="mt-6">
                <p className="text-gray-600">{product.description}</p>
              </div>

              <div className="mt-8">
                <div className="flex items-center justify-between">
                  <span className="text-2xl font-bold text-teal-600">
                    ${product.price}
                    <span className="text-sm font-normal text-gray-500">
                      /{product.unit}
                    </span>
                  </span>
                  <div className="flex items-center space-x-4">
                    <button
                      onClick={() => setQuantity(Math.max(1, quantity - 1))}
                      className="p-2 rounded-full bg-gray-100 hover:bg-gray-200"
                    >
                      <Minus className="w-4 h-4 text-gray-600" />
                    </button>
                    <span className="text-xl font-medium text-gray-900">
                      {quantity}
                    </span>
                    <button
                      onClick={() => setQuantity(quantity + 1)}
                      className="p-2 rounded-full bg-gray-100 hover:bg-gray-200"
                    >
                      <Plus className="w-4 h-4 text-gray-600" />
                    </button>
                  </div>
                </div>
              </div>

              <button
                onClick={handleAddToCart}
                disabled={!product.is_available || product.stock === 0}
                className={`mt-8 w-full py-4 px-6 rounded-lg flex items-center justify-center space-x-2 transition duration-200
                  ${
                    product.is_available && product.stock > 0
                      ? 'bg-teal-600 hover:bg-teal-700 text-white'
                      : 'bg-gray-300 cursor-not-allowed text-gray-500'
                  }`}
              >
                <ShoppingCart className="w-5 h-5" />
                <span>
                  {!product.is_available
                    ? 'Out of Stock'
                    : product.stock === 0
                    ? 'Out of Stock'
                    : 'Add to Cart'}
                </span>
              </button>

              {/* Product Details */}
              {product.details && product.details.length > 0 && (
                <div className="mt-8">
                  <h3 className="text-lg font-semibold text-gray-900">
                    Product Details
                  </h3>
                  <ul className="mt-4 space-y-2">
                    {product.details.map((detail) => (
                      <li
                        key={detail.id}
                        className="flex items-center text-gray-600"
                      >
                        <span className="w-2 h-2 bg-teal-600 rounded-full mr-2"></span>
                        {detail.title}
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Nutrition Info */}
              {product.nutrition && (
                <div className="mt-8">
                  <h3 className="text-lg font-semibold text-gray-900">
                    Nutrition Information
                  </h3>
                  <div className="mt-4 grid grid-cols-2 gap-4">
                    {Object.entries(product.nutrition).map(
                      ([key, value]) =>
                        key !== 'id' && (
                          <div key={key} className="bg-gray-50 p-3 rounded-lg">
                            <div className="text-sm text-gray-500 capitalize">
                              {key}
                            </div>
                            <div className="text-lg font-semibold text-gray-900">
                              {value}
                            </div>
                          </div>
                        )
                    )}
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Alert */}
        {showAlert && (
          <div className="fixed bottom-4 right-4">
            <Alert className="bg-teal-600 text-white">
              <AlertDescription>
                Product added to cart successfully!
              </AlertDescription>
            </Alert>
          </div>
        )}
      </div>
    </div>
  )
}

export default ProductPage
