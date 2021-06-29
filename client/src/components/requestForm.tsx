import React from 'react';
import { Button, Grid, TextField } from '@material-ui/core';
import { RequestFormType } from '../requestForm';
import { Guid } from "guid-typescript";

interface RequestFormProps {
    loading: boolean
    submitRequest: (request: RequestFormType) => void
}

const RequestForm = (props: React.PropsWithChildren<RequestFormProps>) => {
    const { loading, submitRequest: onSubmitRequest } = props;

    const [id, setId] = React.useState("");
    const [username, setUsername] = React.useState("");
    const [password, setPassword] = React.useState("");
    const [idError, setIdError] = React.useState<string>("");
    const [usernameError, setUsernameError] = React.useState<string>("");
    const [passwordError, setPasswordError] = React.useState<string>("");

    const handleonClick = () => {
        const validId = validateId(id);
        const validUsername = validateUsername(username);
        const validPassword = validatePassword(password);
        
        if(!validId || !validUsername || !validPassword){
            return;
        }
        
        const request = {
            id,
            username,
            password
        };

        console.log("request sent");
        onSubmitRequest(request);
    };

    const validateUsername = (username: string) => {
        if (!username || !username.length) {
            setUsernameError("Username cannot be empty");
            return false;
        }

        return true;
    }

    const validatePassword = (password: string) => {
        if (!password || !password.length) {
            setPasswordError("Password cannot be empty");
            return false;
        }

        return true;
    }

    const validateId = (id: string) => {
        if (!id || !id.length) {
            setIdError("Product Id cannot be null");
            return false;
        }

        if (Guid.parse(id).toString() === Guid.EMPTY) {
            setIdError("Product Id is not a valid Guid");
            return false;
        }

        return true;
    }

    const handleUsernameChange = (username: string) => {
        setUsername(username);

        if(!validateUsername(username)){
            return;
        }

        setUsernameError("");
    };

    const handlePasswordChange = (password: string) => {
        setPassword(password);

        if (!validatePassword(password)) {
            return;
        }

        setPasswordError("");
    };

    const handleIdChange = (id: string) => {
        setId(id);

        if (!validateId(id)){
            return;
        }

        setIdError("");
    };

    return (
        <Grid container direction="column" alignItems="center" spacing={4} >
            <Grid item>
                <TextField
                    label="Product Id"
                    value={id}
                    color="secondary"
                    disabled={loading}
                    placeholder="0ee2be67-7b4e-48a2-aad4-71dbefa7471e"
                    onChange={(e) => handleIdChange(e.target.value)}
                    helperText={idError}
                    error={!!idError}
                />
            </Grid>
            <Grid item>
                <TextField
                    label="Username"
                    value={username}
                    color="secondary"
                    InputProps={{
                        disabled: loading

                    }}
                    disabled={loading}
                    onChange={(e) => handleUsernameChange(e.target.value)}
                    helperText={usernameError}
                    error={!!usernameError}
                />
            </Grid>
            <Grid item>
                <TextField
                    label="Password"
                    type="password"
                    color="secondary"
                    value={password}
                    disabled={loading}
                    onChange={(e) => handlePasswordChange(e.target.value)}
                    helperText={passwordError}
                    error={!!passwordError}
                />
            </Grid>
            <Grid item>
                <Button
                    onClick={handleonClick}
                    disabled={loading}
                >
                    Produce JsonLD
                </Button>
            </Grid>
        </Grid>
    );
}

export { RequestForm }