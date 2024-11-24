import subprocess
import os


def run_script(script_path, *args):
    print(f"Running {script_path} with arguments {args}")
    result = subprocess.run(["python", script_path] + list(args), capture_output=True, text=True)
    print(f"Output of {script_path}:")
    print(result.stdout)
    if result.stderr:
        print(f"Error output of {script_path}:")
        print(result.stderr)
    print(f"Finished running {script_path}\n")


def run_task(task_path):
    print(f"Running task {task_path}")
    # Запуск задач
    src_path = os.path.join(task_path, "src")
    tests_path = os.path.join(task_path, "tests")

    for script in os.listdir(src_path):
        if script.endswith(".py"):
            run_script(os.path.join(src_path, script))

    for test in os.listdir(tests_path):
        if test.endswith(".py"):
            run_script(os.path.join(tests_path, test))

    print(f"Finished running task {task_path}\n")


def run_lab(lab_path):
    print(f"Running lab {lab_path}")
    for task in os.listdir(lab_path):
        task_path = os.path.join(lab_path, task)
        if os.path.isdir(task_path):
            run_task(task_path)
    print(f"Finished running lab {lab_path}\n")


def main():
    labs = ["lab1", "lab2"]
    for lab in labs:
        run_lab(lab)


if __name__ == "__main__":
    main()
