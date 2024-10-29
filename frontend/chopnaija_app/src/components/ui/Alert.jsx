// components/ui/Alert.jsx
import React from 'react'
import { cn } from '../../lib/utils'

const Alert = React.forwardRef(
  ({ className, variant = 'default', ...props }, ref) => {
    const baseStyles = 'relative w-full rounded-lg border border-slate-200 p-4'
    const variantStyles = {
      default: 'bg-white text-slate-950',
      destructive: 'border-red-500/50 text-red-500',
    }

    return (
      <div
        ref={ref}
        role="alert"
        className={cn(baseStyles, variantStyles[variant], className)}
        {...props}
      />
    )
  }
)

const AlertDescription = React.forwardRef(({ className, ...props }, ref) => (
  <div ref={ref} className={cn('text-sm', className)} {...props} />
))

Alert.displayName = 'Alert'
AlertDescription.displayName = 'AlertDescription'

export { Alert, AlertDescription }
