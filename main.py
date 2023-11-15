import httpx
from prefect import flow
from prefect.deployments import Deployment


@flow(log_prints=True)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    url = f"https://api.github.com/repos/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    repo = response.json()
    print(f"{repo_name} repository statistics 🤓:")
    print(f"Stars 🌠 : {repo['stargazers_count']}")
    print(f"Forks 🍴 : {repo['forks_count']}")


# if __name__ == "__main__":
    # Deployment.build_from_flow(
        # flow=get_repo_info,
        # name="pipeline_deployment",
        # work_pool_name="kub",
        # apply=True,
    # )

