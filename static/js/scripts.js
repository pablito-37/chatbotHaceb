function sendMessage() {
    var userMessage = document.getElementById("user-input").value;
    if (userMessage.trim() === "") return;

    appendMessage(userMessage, 'user-message', 'user-image', '../static/img/user-profile.png');

    // Hacer una solicitud al servidor para obtener la respuesta
    fetch("/get_response", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ pregunta: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        var chatbotResponse = data.respuesta;
        appendMessage(chatbotResponse, 'bot-message', 'bot-image', '../static/img/bot-profile.png');
    });
}

function sendReport() {
    var reportMessage = document.getElementById("report-input").value;
    if (reportMessage.trim() === "") return;

    // Aquí puedes enviar el reporte al servidor o realizar cualquier acción necesaria
    alert("Reporte enviado: " + reportMessage);
}

function appendMessage(message, messageType, profileImageClass, profileImagePath) {
    var chatBox = document.getElementById("chat-box");
    var newMessageContainer = document.createElement("div");
    newMessageContainer.className = "message-container " + messageType;

    // Agregar imagen de perfil
    var profileImage = document.createElement("img");
    profileImage.src = profileImagePath;
    profileImage.className = "profile-image " + profileImageClass;

    // Añadir la imagen de perfil fuera de la burbuja
    chatBox.appendChild(profileImage);

    var newMessageText = document.createElement("div");
    newMessageText.className = "message-text";
    newMessageText.textContent = message;

    newMessageContainer.appendChild(newMessageText);
    chatBox.appendChild(newMessageContainer);

    // Limpiar el campo de entrada después de enviar un mensaje
    document.getElementById("user-input").value = "";

    // Desplazar el contenedor del chat hacia abajo para mostrar el último mensaje
    chatBox.scrollTop = chatBox.scrollHeight;
}


function sendReport() {
    var reportText = document.getElementById("report-input").value;

    fetch("/submit_report", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ report: reportText }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message); // Muestra el mensaje de respuesta del servidor

        // Muestra una alerta de SweetAlert con el mensaje de éxito del servidor
        Swal.fire({
            icon: 'success',
            title: '¡Reporte realizado exitosamente!',
            // text: data.message
        });

        // Limpiar el contenido del textarea después de enviar el reporte
        document.getElementById("report-input").value = "";
    })
    .catch(error => {
        // Manejar errores si ocurrieron al enviar el reporte
        console.error('Error al enviar el reporte:', error);
        // Mostrar una alerta de SweetAlert indicando que ha ocurrido un error
        Swal.fire({
            icon: 'error',
            title: '¡Error!',
            text: 'Ocurrió un error al enviar el reporte. Por favor, inténtalo de nuevo.'
        });
    });
}
