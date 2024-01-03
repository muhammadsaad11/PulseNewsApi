const BUILD_HOOK = 'https://api.netlify.com/build_hooks/6595038ee4b44f650decfdb7'

export default async (req: Request) => {
    const { next_run } = await req.json()

    await fetch(BUILD_HOOK, {
          method: 'POST'
        }).then((response) => {
          console.log('Build hook response:', response.json())
          console.log("Received event! Next invocation at:", next_run)
        })
      
        return {
          statusCode: 200
        }

    
}