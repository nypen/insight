import React from 'react';
import { CircularProgress, Divider, Grid, makeStyles, Theme, Typography } from '@material-ui/core';
import { AppBar } from './appBar';
import { getUrl } from '../appServices';
import { RequestFormType } from '../requestForm';
import { RequestForm } from './requestForm';
import { githubGist } from 'react-syntax-highlighter/dist/esm/styles/hljs'
import { encode } from "base-64";
import SyntaxHighlighter from 'react-syntax-highlighter';

const useStyles = makeStyles((theme: Theme) => ({
    root: {
        height: "100vh",
        overflowY: "hidden",
        backgroundColor: theme.palette.grey[700],
    },
    requestForm: {
        height: "90vh",
        padding: "1px",
        backgroundColor: "#FFF",
    }

}));

interface MainProps { }

const Main = (props: React.PropsWithChildren<MainProps>) => {
    const [error, setError] = React.useState(null);
    const [loading, setLoading] = React.useState(false);
    const [result, setResult] = React.useState(null);

    const classes = useStyles();

    // const theme = {
    //     main: "line-height:1.3;background:#FFF;overflow:auto;",
    //     key: `color:${purple[700]}`,
    // };

    const handleonClick = (requestForm: RequestFormType) => {
        setLoading(true);
        setResult(null);

        fetch(getUrl(requestForm.id) + "?isSentinel5p=" + requestForm.isSentinel5P.toString(), {
            method: 'GET',
            cache: "no-cache",
            // body: JSON.stringify({ username: requestForm.username, password: requestForm.password, isSentinel5P: requestForm.isSentinel5P }),
            headers: new Headers({
                'mode': 'cors',
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + encode(requestForm.username + ":" + requestForm.password),
            })
        })
            .then(
                (result) => {
                    const jsonResult = result.json()
                    console.log("result " + jsonResult);
                    return jsonResult;
                },
                (error) => {
                    console.log("Error" + error);
                    setLoading(false);
                    setError(error);
                }
            )
            .then(
                // TODO: Fix loading remaining true after error response
                (data) => {
                    setLoading(false);
                    setResult(data);
                    console.log(data)
                }
            )
    }

    return (
        <div>
            <Grid container className={classes.root} justify="center" xs={12}>
                <Grid item xs={12}>
                    <AppBar />
                </Grid>
                <Grid item container className={classes.requestForm} direction="row" justify="center" alignItems="center" xs={10}>
                    <Grid item style={{ width: "45%" }}>
                        <RequestForm
                            loading={loading}
                            submitRequest={handleonClick}
                        />
                    </Grid>
                    <Divider orientation="vertical" style={{ marginRight: "-1px" }} />
                    <Grid item container justify="center" alignItems="center" style={{ width: "55%", height: "inherit", overflow: "auto" }}>
                        <Grid item style={{ width: "100%" }}>
                            {result &&
                                <SyntaxHighlighter
                                    language='json'
                                    showLineNumbers={true}
                                    style={githubGist}
                                    wrapLongLines={true}
                                    wrapLines={true}
                                    lineProps={lineNumber => ({
                                        style: { display: 'block' },
                                        onClick() {
                                        }
                                    })}
                                >
                                    {JSON.stringify(result, null, 2)}
                                </SyntaxHighlighter>
                            }
                            {
                                loading && <CircularProgress size={60} color="secondary" />
                            }
                            <Typography color="error">
                                {error && error.message}
                            </Typography>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
        </div>
    );
}

export { Main }