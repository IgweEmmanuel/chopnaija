import { useState } from 'react'
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardActions,
} from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { X, Plus, Minus } from 'lucide-react'

const formatCurrency = (amount) => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  }).format(amount)
}

const CartItem = ({ item, onRemove, onQuantityChange }) => {
  const [quantity, setQuantity] = useState(item.quantity)

  const handleQuantityChange = (value) => {
    setQuantity(value)
    onQuantityChange(item.id, value)
  }

  return (
    <Card className="flex flex-col md:flex-row items-center justify-between p-4 gap-4 bg-gray-100 rounded-lg shadow-md">
      <div className="flex items-center gap-4">
        <img
          src={item.image}
          alt={item.name}
          className="w-20 h-20 object-cover rounded-md"
        />
        <div>
          <h3 className="text-lg font-medium">{item.name}</h3>
          <p className="text-gray-500">{item.description}</p>
        </div>
      </div>

      <div className="flex items-center gap-4">
        <div className="flex items-center gap-2">
          <Button
            variant="outline"
            onClick={() => handleQuantityChange(quantity - 1)}
            disabled={quantity <= 1}
          >
            <Minus size={16} />
          </Button>
          <Input
            type="number"
            min={1}
            value={quantity}
            onChange={(e) => handleQuantityChange(parseInt(e.target.value))}
            className="w-16 text-center"
          />
          <Button
            variant="outline"
            onClick={() => handleQuantityChange(quantity + 1)}
          >
            <Plus size={16} />
          </Button>
        </div>
        <p className="text-lg font-medium">
          {formatCurrency(item.price * quantity)}
        </p>
        <Button variant="outline" color="red" onClick={() => onRemove(item.id)}>
          <X size={16} />
        </Button>
      </div>
    </Card>
  )
}

export default CartItem
