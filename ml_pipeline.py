from zenml import step,pipeline

@step
def function():
    return "Hello World"

@step
def function2(text):
    return "Hello"+text


@pipeline
def ml_pipeline():
    res = function()
    response = function2(res)
    return response

if __name__=="__main__":
    res = ml_pipeline()
    print("Response")