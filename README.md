## Building Generative AI Applications with SageMaker Foundational Models

Welcome to our hands-on workshop on building generative AI applications using Amazon SageMaker and Jumpstart Notebooks with foundational models. In this interactive session, you will learn how to harness the power of AI to create innovative, scalable, and user-friendly solutions for text and image generation tasks. You will be building a tool that will enable content authors to generate attractive images and taglines for their articles.

![The deployed app, that takes text from an article and creates a tagline with a cover image](./build_on_poster_example.png)

Throughout the workshop, we will guide you through three key steps to develop and deploy your application:

1. Deploy a Foundational Model: We will walk you through using a SageMaker Jumpstart Notebook to deploy a state-of-the-art foundational model for text and image generation tasks.

2. Integrate with AWS Lambda: In this step, you will learn how to create and deploy an AWS Lambda function that leverages the SageMaker model endpoint. This integration will enable seamless communication between your application and the deployed AI model, ensuring efficient processing of user inputs.

3. Deploy a Front-End Application: Finally, we will demonstrate how to deploy a user-friendly front-end application that interacts with the deployed model endpoint. This application will allow users to experience the full potential of your AI-powered solution.

By the end of this workshop, you will have gained valuable hands-on experience in deploying and integrating cutting-edge AI models with AWS services to build creative and engaging applications.

Here is the link to the [workshop](https://catalog.workshops.aws/building-gen-ai-apps-with-found-models/en-US)

### Building the Docker Image

**Note:** If you are running the CloudFormation in your own account, you must build the Docker image first, and push to your own ECR repo. Then update the template with the image name on line [19](https://github.com/build-on-aws/building-gen-ai-apps-with-found-models-workshop/blob/main/ai-gen-workshop-cfn.yml#L19). 

To build the image you must have [Docker](https://docs.docker.com/get-docker/) installed.

Then you can run
```bash
docker build . -t build_on_poster
```

More details can be found here on how to push the image yo your account: https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

