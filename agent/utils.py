def build_summary(project_info, analysis):

    text = []

    text.append(f"Project: {analysis['project_name']}")
    text.append(f"Express: {analysis['express']}")
    text.append(f"Mongoose: {analysis['mongoose']}")

    text.append("\nModels:")
    for f in project_info["models"]:
        text.append(f"- {f}")

    text.append("\nControllers:")
    for f in project_info["controllers"]:
        text.append(f"- {f}")

    text.append("\nRoutes:")
    for f in project_info["routes"]:
        text.append(f"- {f}")

    return "\n\n".join(text)