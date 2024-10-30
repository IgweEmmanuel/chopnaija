import ClipLoader from 'react-spinners/ClipLoader'

const override = {
  display: 'block',
  margin: '0 auto',
  borderColor: '#51A262',
}

const Spinner = ({ loading }) => {
  return (
    <ClipLoader
      loading={loading}
      cssOverride={override}
      size={450}
      aria-label="Loading Spinner"
      data-testid="loader"
    />
  )
}

export default Spinner
