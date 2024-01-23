const BUILD_HOOK = 'https://api.netlify.com/build_hooks/6595038ee4b44f650decfdb7'

// export default async (req: Request) => {
//     const { next_run } = await req.json()

//     await fetch(BUILD_HOOK, {
//           method: 'POST'
//         }).then((response) => {
//           console.log('Build hook response:', response.json())
//           console.log("Received event! Next invocation at:", next_run)
//         })
      
//         return {
//           statusCode: 200
//         }

    
// }


export default async (req) => {
  const { next_run } = await req.json();

  // Check if the request is from Netlify scheduler
  const isNetlifyScheduler = req.headers['X-Netlify-Scheduler'] === 'true';

  if (isNetlifyScheduler) {
    await fetch(BUILD_HOOK, {
      method: 'POST',
    }).then((response) => {
      console.log('Build hook response:', response.json());
      console.log('Received event! Next invocation at:', next_run);
    });
  }

  return {
    statusCode: 200,
  };
};