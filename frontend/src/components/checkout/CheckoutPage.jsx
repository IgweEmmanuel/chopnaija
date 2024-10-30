import OrderSummary from "./OrderSummary"
import PaymentSection from "./PaymentSection"
import useCartData from "../../hooks/useCartData"
import Spinner from "../ui/Spinner"

const CheckoutPage = () => {

    const  {cartitems, setCartItems, cartTotal, setCartTotal, loading, tax} = useCartData()

    if(loading){
            return <Spinner loading={loading} />
    }

  return (
    <div className="container my-3">

      <div className="row">
        <OrderSummary cartitems={cartitems} cartTotal={cartTotal} tax={tax} />
        <PaymentSection />
      </div>
    </div>
  )
}

export default CheckoutPage






