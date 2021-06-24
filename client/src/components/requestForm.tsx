import React from 'react';
import { Button, FormControl, FormHelperText, Grid, Input, InputLabel } from '@material-ui/core';
import { RequestFormType } from '../types';
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
        const request = {
            id,
            username,
            password
        };

        if (!id.length || !username.length || !password.length) {
            return;
        }

        if (!!idError.length || !!usernameError.length || !!passwordError.length) {
            return;
        }
        console.log("what");

        onSubmitRequest(request);
    };

    const handleUsernameChange = (username: string) => {
        setUsername(username);

        if (!username || !username.length) {
            setUsernameError("Username cannot be empty");
            return;
        }

        setUsernameError("");
    };

    const handlePasswordChange = (password: string) => {
        setPassword(password);

        if (!password || !password.length) {
            setPasswordError("Password cannot be empty");
            return;
        }

        setPasswordError("");
    };

    const handleIdChange = (id: string) => {
        setId(id);

        if (!id || !id.length) {
            setIdError("Product Id cannot be null");
            return;
        }

        if (Guid.parse(id).toString() === Guid.EMPTY) {
            setIdError("Product Id is not a valid Guid");
            return;
        }

        setIdError("");
    };

    return (
        <Grid container direction="column" alignItems="center" spacing={6} justify="flex-end" >
            <Grid item>
                <FormControl error={!!idError}>
                    <InputLabel>Id</InputLabel>
                    <Input
                        value={id}
                        color="secondary"
                        disabled={loading}
                        placeholder="0ee2be67-7b4e-48a2-aad4-71dbefa7471e"
                        onChange={(e) => handleIdChange(e.target.value)}
                    />
                    <FormHelperText>{idError}</FormHelperText>
                </FormControl>
            </Grid>
            <Grid item>
                <FormControl error={!!usernameError}>
                    <InputLabel>Username</InputLabel>
                    <Input
                        color="secondary"
                        value={username}
                        disabled={loading}
                        onChange={(e) => handleUsernameChange(e.target.value)}
                    />
                    <FormHelperText>{usernameError}</FormHelperText>
                </FormControl>
            </Grid>
            <Grid item>
                <FormControl error={!!passwordError}>
                    <InputLabel>Password</InputLabel>
                    <Input
                        color="secondary"
                        value={password}
                        disabled={loading}
                        onChange={(e) => handlePasswordChange(e.target.value)}
                    />
                    <FormHelperText>{passwordError}</FormHelperText>
                </FormControl>
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